
import TokenKind
import Tokenizer

import Maths
import expressioncheck


class MyClass:
    def method(self):
        filename = 'input.txt'
        Global = {}

        with open(filename) as f:
            lines = f.readlines()

        for l in lines:

            tokens = []
            tokenizer = Tokenizer.Tokenizer(l)
            token = tokenizer.GetToken()
            tokens.append(token)

            while token.kind != TokenKind.TokenKind.end:
                firstpart, secondpart = (str(token.kind)).split(".")
                # print(secondpart + ": " + token.text)
                token = tokenizer.GetToken()
                tokens.append(token)

            singleinput = False
            output = expressioncheck.getexpression(tokens, Global, singleinput)
            expressionvalidity = output[0]
            stringvalidity = output[1]
            inputvalidity = output[3]
            statementtokens = []
            variabletokens = output[2]



            if inputvalidity:
                if len(tokens) == 5:
                    if str(tokens[3].kind) == "TokenKind.string":
                        inputstring = str(tokens[3].text)
                        userinput = input(inputstring)

                    else:
                        userinput = input("")

                else:
                    userinput = input()

                inputokens = []
                tokenizer = Tokenizer.Tokenizer(userinput)
                inputoken = tokenizer.GetToken()
                inputokens.append(inputoken)

                while inputoken.kind != TokenKind.TokenKind.end:
                    inputoken = tokenizer.GetToken()
                    inputokens.append(inputoken)

                singleinput = True
                inputoutput = expressioncheck.getexpression(inputokens, Global,singleinput)
                singleinput = False
                expressionvalidity = inputoutput[0]
                stringvalidity = inputoutput[1]



                if expressionvalidity:
                    inputexpression = ""
                    for tk in inputokens:
                        inputexpression += str(tk.text)
                    # Maths.calculate(str(tokenizer.text))
                    result = Maths.calculatevariable(inputexpression)
                    if str(tokens[0].text) in Global:
                        Global[str(tokens[0].text)] = result
                        expressionvalidity = False
                    elif str(tokens[0].text) not in Global:
                        Global[str(tokens[0].text)] = result
                        inputvalidity = False
                        expressionvalidity = False

                    else:
                        print("ERROR: Identifier not assigned or not existent")
                        inputvalidity = False
                        expressionvalidity = False
                elif stringvalidity:
                    stringinputexpression =[]
                    for tk in inputokens:
                        stringinputexpression.append(str(tk.text))
                        # Maths.calculate(str(tokenizer.text))
                    result = Maths.calculatestringvariable(stringinputexpression)
                    if str(tokens[0].text) in Global:
                        Global[str(tokens[0].text)] = result
                        stringvalidity = False
                    elif str(tokens[0].text) not in Global:
                        Global[str(tokens[0].text)] = result
                        inputvalidity = False
                        stringvalidity = False

                    else:
                        print("ERROR: Identifier not assigned or not existent")
                        inputvalidity = False
                        stringvalidity = False



            if expressionvalidity:
                expression = ""
                validity = True

                if variabletokens:
                    for tk in variabletokens:
                        if str(tk.kind) == "TokenKind.identifier":
                            if str(tk.text) in Global:
                                text = Global[str(tk.text)]
                                expression += text
                            else:
                                print("ERROR: variable " + str(tk.text) + " not existent")
                                validity = False

                                break
                        else:
                            expression += str(tk.text)
                    # Maths.calculate(str(tokenizer.text))

                    if validity:
                        result = Maths.calculatevariable(expression)
                        if str(tokens[0].text) in Global:
                            Global[str(tokens[0].text)] = result
                            # print(Global[str(tokens[1].text)])
                        else:
                            Global[str(tokens[0].text)] = result
                            # print(Global[str(tokens[1].text)])

                else:
                    for tk in tokens:
                        expression += str(tk.text)
                       # if "true" in expression:
                       #    expression.replace("true", "t")
                       # elif "false" in expression:
                       #   expression.replace("false", "f")

                    # Maths.calculate(str(tokenizer.text))
                    Maths.calculate(expression)
                variabletokens = []


            elif stringvalidity:
                validity = True
                stringexpression = []
                count = 0
                if variabletokens:
                    for tk in variabletokens:
                        if str(tk.kind) == "TokenKind.identifier":
                            if str(tk.text) in Global:
                                if Global[str(tk.text)] == "True" or Global[str(tk.text)] == "False":
                                    if Global[str(tk.text)] == "True":
                                        text = "t"
                                    else:
                                        text = "f"
                                else:
                                    text = Global[str(tk.text)]
                                stringexpression.append(text)
                            else:
                                print("ERROR: variable " + str(tk.text) + "not existent")
                                validity = False
                                break
                        else:
                            stringexpression.append(str(tk.text))
                    # stringexpression.append(str(tk.text))
                    # Maths.calculate(str(tokenizer.text))
                    result = Maths.calculatestringvariable(stringexpression)
                    if validity:
                        if str(tokens[0].text) in Global:
                            Global[str(tokens[0].text)] = result
                            # print(Global[str(tokens[1].text)])
                        else:
                            Global[str(tokens[0].text)] = result
                            # print(Global[str(tokens[1].text)])
                        variabletokens = []
                else:
                    for tk in tokens:
                        if count == 0:
                            stringexpression.append(str(tk.text))
                            count += 1
                        else:
                            stringexpression.append(str(tk.text))
                    Maths.calculatestring(stringexpression)

        #print(Global)


if __name__ == "__main__":
    MyClass().method()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
