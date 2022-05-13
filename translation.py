from googletrans import Translator

translator = Translator()
sentence = input("언어를 감지할 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요? ")
result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("\n============= 출력 결과 ============\n")
print(detected.lang,":", sentence)
print(result.dest,":", result.text)
print("\n====================================\n")