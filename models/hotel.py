from sql_alchemy import banco


class HotelModel(banco.Model):
    __tablename__ = 'hoteis' #estancia a tabela

    #estancia as colunas dessa tabela abaixo
    hotel_id = banco.Column(banco.String, primary_key=True)#instancioando chave primario no hotel ID
    nome = banco.Column(banco.String(80))#estancia o nome com 80 caracteres
    estrelas = banco.Column(banco.Float(precision=1))#estancia estrelas com uma casa depois da virgula
    diaria = banco.Column(banco.Float(precision=2))#estancia diaria com duas casa depois da virgula
    cidade = banco.Column(banco.String(40))#estancia com 40 caracteres o nome da cidade


    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.hotel_id = hotel_id
        self.nome = nome
        self.estrelas = estrelas
        self.diaria = diaria
        self.cidade = cidade

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrela': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }