from config_bot import dp,bot
from aiogram import types
import candy as cy
import log



@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id, text=f'{message.from_user.username}'
                                                      f', привет мой хороший!')
    await bot.send_message(message.from_user.id, text=f'{cy.whosFirst(message.from_user.username,message.from_user.id)}')
    await bot.send_message(message.from_user.id, text=cy.info())
    if cy.getFirstTurnComp():
        await bot.send_message(message.from_user.id, text=cy.getCompTurn())

@dp.message_handler()
async def anything(message: types.Message):
    if cy.checkMessage(message.text):
        cy.getHumanTurn(int(message.text))
        checkUser=cy.checkWin()
        if checkUser:

            log.saveBattle(cy.getStrToLog(message.from_user.id, 'message.from_user.username'))
            await bot.send_message(message.from_user.id, text=f'Победил {message.from_user.username}!')
            await bot.send_message(message.from_user.id, text=cy.whosFirst(message.from_user.username,message.from_user.id))
            await bot.send_message(message.from_user.id, text=cy.info())
            if cy.getFirstTurnComp():
                await bot.send_message(message.from_user.id, text=cy.getCompTurn())
        else:
            if cy.getFirstTurnComp():
                await bot.send_message(message.from_user.id, text=cy.info())
            await bot.send_message(message.from_user.id, text=cy.getCompTurn())
            checkComp=cy.checkWin()
            if checkComp:
                log.saveBattle(cy.getStrToLog(message.from_user.id,'bot'))
                await bot.send_message(message.from_user.id, text=f'Победил bot!')
                await bot.send_message(message.from_user.id, text=cy.whosFirst(message.from_user.username,message.from_user.id))
                await bot.send_message(message.from_user.id, text=cy.info())
                if cy.getFirstTurnComp():
                    await bot.send_message(message.from_user.id, text=cy.getCompTurn())
            else:
                if not cy.getFirstTurnComp():
                    await bot.send_message(message.from_user.id, text=cy.info())
    else:
        await message.reply(cy.getError())