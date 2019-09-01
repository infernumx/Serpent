local commands = {
	online = {rawargs = false, callback = function()
		local online = {}
		for _, player in ipairs(Game.getPlayers()) do
			online[#online+1] = player:getName()
		end
		return (#online > 0) and table.concat(online, '\n') or 'Nobody'
	end}
}

do
	local dataTypes = {
	    number = result.getNumber,
	    string = result.getString,
	    stream = result.getStream
	}

	function queryToTable(id, values)
	    local ret = {}
	    if not id then
	        return ret
	    end
	    repeat
	        local t = {}
	        for i = 1, #values do
	            local column, dataType = values[i]:match('(%a+):(%a+)')
	            t[column] = dataTypes[dataType](id, column)
	        end
	        ret[#ret+1] = t
	    until not result.next(id)
	    return ret
	end
end

function enqueue(event, args)
	local query = string.format('INSERT INTO `server_listener` (`id`, `command`, `arguments`) VALUES (NULL, "%s", "%s")', event, args)
	db.query(query)
end

do
	local function event_listener()
		local queue = db.storeQuery('SELECT * FROM `bot_listener`')
		if queue then
			local results = queryToTable(queue, {'id:number', 'command:string', 'arguments:string'})
			for i = 1, #results do
				local r = results[i]
				local command = commands[r.command]
				if command then
					local args = r.arguments
					if not command.rawargs then
						args = string.split(r.arguments, ',')
						for i = 1, #args do
							args[i] = args[i]:trim()
						end
					end
					local ret = command.callback(args)
					if ret then
						enqueue(r.command, ret)
					end
				end
				db.query('DELETE FROM `bot_listener` WHERE `id` = '.. r.id)
			end
			result.free(queue)
		end
		listener_id = addEvent(event_listener, 1000)
	end

	if listener_id then
		stopEvent(listener_id)
	end

	addEvent(event_listener, 1000) -- let libs load again before running listener
end
