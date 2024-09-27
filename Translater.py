#python code translator
from googletrans import Translator
translator = Translator()

def translate_to_bangla(text):
    translation = translator.translate(text, dest='bn')
    return translation.text

if __name__ == "__main__":
    english_text = """
    1. Function Definition
    def simpleArraySum(ar):
        # Return the sum of the array elements
        return sum(ar)

    2. Reading Input
    n = int(input())
    This line reads input from the user using input() and converts it to an integer using int().
    The variable n holds the size of the array (though it's not used in the rest of the code).

    3. Reading and Processing the Array Elements
    ar = list(map(int, input().split()))
    input() reads a line of space-separated values entered by the user.
    """

    bangla_translation = translate_to_bangla(english_text)

    print("Translated text in Bangla:\n", bangla_translation)


