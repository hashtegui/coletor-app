from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.metrics import dp
from src.dao.usuario import UsuarioDao



class LoginWindow(Screen):

    def __init__(self, **kw):
        super(LoginWindow, self).__init__(**kw)

    def abrir_popup(self):
        login = self.ids.login.text
        senha = int(self.ids.senha.text)
        ud = UsuarioDao()
        usuario_logado = ud.logar(login, senha)

        if usuario_logado:
            self.parent.current = 'dash'
        else:
            close_button = Button(text='fechar')
            layout = GridLayout(cols=1, spacing=10, padding=10)
            layout.add_widget(close_button)
            pop = Popup(title='Erro no Login',
                        content=layout,
                        size_hint=(None, None),
                        size=(dp(200), dp(200)))
            pop.open()

            close_button.bind(on_press=pop.dismiss)
          #     if log.login(login.text,int(senha.text)):\
            #     app.root.current = "dash";\
            #     else Factory.Teste().open();
