import os
from tarefa_dao import TarefaDAO
from usuario_dao import UsuarioDAO
from tarefa import *

class Main(object):
    
    @staticmethod
    def main():
        os.system('color f')
        Main.autenticacao()
        usuario_autenticado = UsuarioDAO.get_instance().buscar_todos()
        while True:
            os.system('cls')
            print('Bem-Vindo {}'.format(usuario_autenticado[0]))
            print('[1] - Adicionar Tarefa')
            print('[2] - Listar Tarefas')
            print('[3] - Trocar Status Tarefa')
            print('[4] - Remover  Tarefa')
            print('[5] - Configurações')
            print('[6] - Sair\n')
            try:
                opcao = input('\nDigi1te sua opcao: ')
                if opcao == '1':
                    Main.adicionar_tarefa()
                elif opcao == '2':
                    Main.listar_tarefas()
                    input('\nAperte enter tecla para continuar...')
                elif opcao == '3':
                    Main.listar_tarefas()
                    Main.trocar_status()
                elif opcao == '4':
                    Main.listar_tarefas()
                    Main.remover_tarefa()
                elif opcao == '5':
                    Main.configuracoes()
                elif opcao == '6':
                    break
                else:
                    input('Opcao invalida! Aperte enter para continuar...')
                    
            except Exception as e:
                raise e
                #raise Exception('Opção inválida!')

            
    @staticmethod
    def adicionar_tarefa():
        os.system('cls')
        text = input('Digite o nome da tarefa: ')
        TarefaDAO.get_instance().persistir(Tarefa(0, text))

    @staticmethod
    def listar_tarefas():
        os.system('cls')
        for dado in TarefaDAO.get_instance().buscar_todos():
            if dado[2] == 'True':
                print('\033[32mID: {} \t{} \tCompleto: {}\33[m'.format(dado[0], dado[1], dado[2]))
            else:
                print('\033[31mID: {} \t{} \tCompleto: {}\33[m'.format(dado[0], dado[1], dado[2]))

    @staticmethod
    def trocar_status():
        try:
            identificador = int(input('\nDigite o ID da tarefa: '))
            query = TarefaDAO.get_instance().buscar(identificador)
            if query != None:
                tarefa = Tarefa(query[0], query[1])
                tarefa.completed = True if query[2] == 'False' else 'False'
                TarefaDAO.get_instance().persistir(tarefa)
        except Exception as e:
            print('ID invalido!')

        finally:
            input('Aperte enter para continuar...')

    @staticmethod
    def remover_tarefa():
        try:
            identificador = int(input('\nDigite o ID da tarefa: '))
            TarefaDAO.get_instance().deletar(identificador)
        except:
            print('ID invalido para exclusão!')
        
            input('Aperte enter para continuar...')

    @staticmethod
    def autenticacao():
        print('Autenticação\n')
        while True:
            os.system('cls')
            username = input('Digite o nome de usuário: ')
            password = input('Digite a senha: ')
            usuario_banco = UsuarioDAO.get_instance().buscar_todos()
            if (usuario_banco[1] == username) and (usuario_banco[2] == password):
                break
            else:
                print('\033[31m\nO usuário ou a senha está incorreta!\33[m')
                input('Tecle enter para continuar...')

    @staticmethod
    def configuracoes():
        os.system('cls')
        nome = input('Digite o nome: ')
        novo_username = input('Digite o novo username: ')
        nova_senha = input('Digite a nova senha: ')
        UsuarioDAO.get_instance().persistir((nome, novo_username, nova_senha))



if __name__ == "__main__":
    Main.main()