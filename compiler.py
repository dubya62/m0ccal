
import lexer
import normalizer
import preprocessor

if __name__ == "__main__":
    FILENAME = "example.ccal"

    print("++++++++++++++++++++++++++++++")
    print("Lexing...")
    tokens = lexer.lex(FILENAME)
    print(tokens)

    print("++++++++++++++++++++++++++++++")
    print("Normalizing...")
    tokens = normalizer.normalize(tokens, FILENAME)
    print(tokens)

    print("++++++++++++++++++++++++++++++")
    print("Preprocessing...")
    tokens = preprocessor.preprocess(tokens, FILENAME)
    print(tokens)



