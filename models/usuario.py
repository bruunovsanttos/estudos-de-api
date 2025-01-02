from sql_alchemy import banco


class UserModel(banco.Model):
    __tablename__ = 'usuarios' #estancia a tabela

    #estancia as colunas dessa tabela abaixo
    user_id = banco.Column(banco.Integer, primary_key=True)#instancioando chave primario no hotel ID
    login = banco.Column(banco.String(40))#estancia o nome com 80 caracteres
    senha = banco.Column(banco.String(40))


    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

    def json(self):
        return {
            'user_id': self.hotel_id,
            'login': self.login
        }

    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id=user_id).first()  #selec * from hoteis where hotel_id = hotel_id
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)# adiciona o objeto ao banco de dados
        banco.session.commit()

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()