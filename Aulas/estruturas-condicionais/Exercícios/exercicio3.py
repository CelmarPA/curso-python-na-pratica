correct_username = "admin"
correct_password = "python2025"

input_username = input("Informe o nome de usuário: ")
input_password = input("Informe a senha: ")

if input_username == correct_username and input_password == correct_password:
    print("Login bem sucedido!")

elif input_username != correct_username and input_password != correct_password:
    print("Credenciais incorretas.")

elif input_username != correct_username:
    print("Username incorreto!")

else:
    print("Senha incorreta!")
