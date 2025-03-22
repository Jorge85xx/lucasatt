from databse import Databse  

def main():
    db = Databse()

    db.add_pessoa('11111111111', 'Cooper')
    db.add_pessoa('22222222222', 'Brand')
    db.add_pessoa('33333333333', 'Murph')
    db.add_pessoa('44444444444', 'TARS')
    db.add_pessoa('55555555555', 'CASE')

    db.add_contato(11987654321, '11111111111')  
    db.add_contato(21987654321, '22222222222')  
    db.add_contato(31987654321, '33333333333')  
    db.add_contato(41987654321, '44444444444')  
    db.add_contato(51987654321, '55555555555')  

    
    pessoa = db.get_pessoa('66666666666')
    if pessoa is not None:
        print(pessoa.nome)
    else:
        print("Pessoa com CPF '66666666666' NÃO EXISTE")

    print("\nLista de Contatos dos Personagens de Interstellar:")
    db.listar_contatos()

if __name__ == '__main__':
    main()
