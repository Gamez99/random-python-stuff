from win11toast import toast

def send_notification(text: str, *, title: str = '', icon: str = '', on_click: str = ''):
    toast(title, text, on_click=on_click, icon=icon)

send_notification("Hello", title="Python Test", on_click='https://pypi.org/project/win11toast/')
