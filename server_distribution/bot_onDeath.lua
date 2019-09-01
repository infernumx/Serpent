local deathEvent = CreatureEvent('bot_onDeath')

function deathEvent.onDeath(creature, corpse, killer)
	local data = {
		creature:getName(),
		creature:getLevel(),
		killer and killer:getName() or 'Unknown',
		os.date('%A, %B %d [%I:%M:%S %p]')
	}
	enqueue('death', table.concat(data, ', '))
	return true
end

deathEvent:type('death')
deathEvent:register()

local loginEvent = CreatureEvent('loginEvent')

function loginEvent.onLogin(player)
	player:registerEvent('bot_onDeath')
	return true
end

loginEvent:type('login')
loginEvent:register()