from uuid import uuid4
from nicegui import ui



messages=[]

@ui.refreshable
def chat_message(own_id):
    for user_id, avatar, text in messages:
        ui.chat_message(avatar=avatar,text=text,sent=user_id==own_id)

@ui.page('/')
def index():
    def send():
        messages.append((user, avatar, text.value))
        chat_message.refresh()
        text.value=''

    user=str(uuid4())
    avatar=f'https://robohash.org/{user}?bgset=bg2'
    with ui.column().classes('w-full item-stretch'):
        chat_message(user)

    with ui.footer().classes('bg-white'):
        with ui.row().classes('w-full item-center'):
            with ui.avatar():
                ui.image(avatar)
            text=ui.input(placeholder='message')\
            .props('rounded outlined').classes('flex-grow')\
            .on('keydown.enter',send)

ui.run()