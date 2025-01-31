def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."
  elif not tem_letra_maiuscula == senha.isupper():
    return f"A senha deve conter pelo menos uma letra maiúscula (A-Z)."
  elif not tem_letra_minuscula == senha.islower():
    return f"A senha deve conter pelo menos uma letra minúscula (a-z)."
  elif not tem_numero == senha.isdigit():
    return f"A senha deve conter pelo menos um número (0-9)."
  elif not tem_caractere_especial == senha.isalnum():
    return f"A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc."
  else:
    return f"Sua senha atende aos requisitos de seguranca. Parabens!"
  

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)