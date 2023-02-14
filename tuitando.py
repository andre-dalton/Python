# texto = ((input()))
# if len(texto) <= 500:
#   if len(texto) < 140:
#     print("TWEET")
#   else:
#     print("MUTE")
print("MUTE" if len(input())>140 else "TWEET") 