import Token
import TokenKind



class Tokenizer:

    def __init__(self, text):
         self.text = text
         self.cursor = 0

    def tokenizer(self):
        return self.text



    def GetToken(self):
        def checkprintable(text):
            printable = text.isprintable()
            return printable

        while(self.cursor< len(self.text)):
            txt = self.text[self.cursor]
            logical =['&','|','<','>','<=','>=','==','!=','true','false','!']

            match txt:
                case '{':
                    self.cursor = self.cursor + 1
                    return Token.Token(self.text[self.cursor - 1], TokenKind.TokenKind.brackets)
                case '}':
                    self.cursor = self.cursor + 1
                    return Token.Token(self.text[self.cursor - 1], TokenKind.TokenKind.brackets)
                case ' ':
                    self.cursor = self.cursor + 1

                case '\t':
                    self.cursor = self.cursor + 1
                case '\f':
                    self.cursor = self.cursor + 1
                case '\n':
                    self.cursor = self.cursor + 1
                case '\r':
                    self.cursor = self.cursor + 1

                case '=':
                    stringHead = self.cursor
                    self.cursor += 1
                    if self.text[self.cursor] == "=":
                        self.cursor += 1
                        stringTail = self.cursor

                        return Token.Token(self.text[stringHead:stringTail], TokenKind.TokenKind.logical)
                    else:
                        return Token.Token(self.text[self.cursor-1], TokenKind.TokenKind.assignment)

                case '!':
                    stringHead = self.cursor
                    self.cursor += 1
                    if self.text[self.cursor] == "=":
                        self.cursor += 1
                        stringTail = self.cursor
                        return Token.Token(self.text[stringHead:stringTail], TokenKind.TokenKind.logical)
                    else:
                        return Token.Token(self.text[self.cursor - 1], TokenKind.TokenKind.arithmetic)


                case '"':
                    self.cursor = self.cursor + 1
                    stringHead = self.cursor

                    while self.cursor < len(self.text):
                        if self.text[self.cursor] == '"':
                            stringTail = self.cursor
                            self.cursor = self.cursor + 1
                            if self.text[stringHead] == " " and self.text[stringHead + 1] == '"':
                                space = "$p4c£"
                                return Token.Token(space, TokenKind.TokenKind.string)
                            else:
                                return Token.Token(self.text[stringHead:stringTail], TokenKind.TokenKind.string)
                        self.cursor = self.cursor + 1
                case _:
                    if self.text[self.cursor].isalpha():
                        indentifierStart = self.cursor
                        self.cursor = self.cursor + 1

                        while self.cursor < len(self.text) and self.text[self.cursor].isspace() == False:
                            self.cursor = self.cursor + 1
                        if self.text[indentifierStart:self.cursor] == "while" or self.text[indentifierStart:self.cursor] == "if":
                            return Token.Token(self.text[indentifierStart], TokenKind.TokenKind.controlflow)

                        elif self.text[indentifierStart:self.cursor] == "false" or self.text[indentifierStart:self.cursor] == "true":
                            return Token.Token(self.text[indentifierStart], TokenKind.TokenKind.logical)
                        elif self.text[indentifierStart:self.cursor] == "input":
                            return Token.Token(self.text[indentifierStart], TokenKind.TokenKind.input)
                        else:
                            #printable = checkprintable(self.text[indentifierStart:self.cursor)
                            return Token.Token(self.text[indentifierStart:self.cursor], TokenKind.TokenKind.identifier)


                    elif self.text[self.cursor].isdigit():
                        indentifierStart = self.cursor
                        self.cursor = self.cursor + 1
                        notonedigit = True
                        while self.cursor < len(self.text) and self.text[self.cursor].isdigit() and self.text[self.cursor].isspace() == False:
                            self.cursor = self.cursor + 1
                            notonedigit = False

                        if notonedigit:
                             return Token.Token(self.text[indentifierStart], TokenKind.TokenKind.num)
                        else:
                        # printable = checkprintable(self.text[indentifierStart:self.cursor)
                            return Token.Token(self.text[indentifierStart:self.cursor], TokenKind.TokenKind.num)


                    elif self.text[self.cursor] in {'+','-','*','/','(',')','.','='}:
                        self.cursor = self.cursor + 1
                        return Token.Token(self.text[self.cursor - 1], TokenKind.TokenKind.arithmetic)
                    elif self.text[self.cursor] in logical:
                        self.cursor = self.cursor + 1
                        return Token.Token(self.text[self.cursor - 1], TokenKind.TokenKind.logical)

                    else:
                        print("Error: " + str(self.text[self.cursor]) + " is not a supported character")
                        self.cursor = self.cursor + 1





        return Token.Token("",TokenKind.TokenKind.end)


