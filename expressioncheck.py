def getexpression(tokens, Global, singleinput):
    # expression calculation
    expressionvalidity = True
    stringvalidity = True
    inputvalidity = True
    tokencontrolflow = False
    tokenbrackets = False
    tokenstring = False
    tokenlogical = False
    tokenend = False
    tokenarithmetic = False
    tokennum = False
    tokenassignment = False
    tokenidentifier = False
    tokeninput = False
    variabletokens = []

    for tk in tokens:

        if str(tk.kind) == "TokenKind.identifier":
            tokenidentifier = True
        elif str(tk.kind) == "TokenKind.controlflow":
            tokencontrolflow = True
        elif str(tk.kind) == "TokenKind.brackets":
            tokenbrackets = True
        elif str(tk.kind) == "TokenKind.arithmetic":
            tokenarithmetic = True
        elif str(tk.kind) == "TokenKind.logical":
            tokenlogical = True
        elif str(tk.kind) == "TokenKind.num":
            tokennum = True
        elif str(tk.kind) == "TokenKind.string":
            tokenstring = True
        elif str(tk.kind) == "TokenKind.end":
            tokenend = True
        elif str(tk.kind) == "TokenKind.assignment":
            tokenassignment = True
        elif str(tk.kind) == "TokenKind.input":
            tokeninput = True


    if tokenidentifier and tokeninput and tokenassignment:
        if str(tokens[0].kind) == "TokenKind.identifier" and str(tokens[1].kind) == "TokenKind.assignment" and str(tokens[2].kind) == "TokenKind.input":
            if tokenarithmetic or tokennum or tokenlogical:
                expressionvalidity = False
                stringvalidity = False
                inputvalidity = False
                print("ERROR: Invalid character after input")
            else:
                expressionvalidity = False
                stringvalidity = False

        else:
            expressionvalidity = False
            stringvalidity = False
            inputvalidity = False
            print("ERROR: Invalid character after input")

    elif tokennum and not tokenidentifier and not tokenlogical and not tokenassignment and not tokenstring and not tokenarithmetic:
        stringvalidity = False
        inputvalidity = False

        if len(tokens) == 2 and not singleinput:
            print(str(tokens[0].text))
        elif len(tokens) == 2 and singleinput:
            pass
        else:
            print("invalid sequence of character, int")
    elif not tokennum and not tokenidentifier and not tokenlogical and not tokenassignment and tokenstring and not tokenarithmetic:
        expressionvalidity = False
        inputvalidity = False
        if len(tokens) == 2 and not singleinput:
            print(str(tokens[0].text))
        elif len(tokens) == 2 and singleinput:
            pass
        else:
            print("invalid sequence of character, string")
    elif not tokennum and tokenidentifier and not tokenlogical and not tokenassignment and not tokenstring and not tokenarithmetic:
        expressionvalidity = False
        stringvalidity = False
        inputvalidity = False
        if len(tokens) == 2:
            print(Global[tokens[0].text])
        elif str(tokens[0].text) == "display" and str(tokens[1].text) in Global:
            if Global[str(tokens[1].text)] == "":
                print("'" + str(tokens[1].text + "' variable is empty"))
            else:
                print(Global[str(tokens[1].text)])
        elif str(tokens[0].text) == "display" and not str(tokens[1].text) in Global:
            print("ERROR: '" + str(tokens[1].text + "' variable is not assigned or not existent"))
        else:
            print("invalid sequence of character, indentifier")
    elif not tokenidentifier and not tokenassignment:

        if tokennum and tokenend or (tokenlogical or tokenarithmetic):
            if tokennum and tokenstring:
                stringvalidity = False
                expressionvalidity = False
                inputvalidity = False
                print("ERROR: string value cannot be compared to a int")
            elif (tokenlogical or tokenarithmetic) and not (tokennum or tokenstring):
                if tokenlogical:
                    trueorfalse = False
                    for tk in tokens:
                        if str(tk.text) == "t" or str(tk.text) == "f":
                            trueorfalse = True
                    if trueorfalse:
                        stringvalidity = False
                        inputvalidity = False
                    else:
                        print("ERROR: No valid operands in the expression")
            elif (tokennum and tokenend) and (tokenlogical or tokenarithmetic):
                stringvalidity = False
                inputvalidity = False


            elif (tokenstring and tokenend) and (tokenlogical or tokenarithmetic):
                expressionvalidity = False
                inputvalidity = False
        else:
            print("ERROR: not a valid sequence of character")
            expressionvalidity = False
            stringvalidity = False
            inputvalidity = False

    elif tokenidentifier or tokenassignment:

        if tokenidentifier and tokenassignment:

            if str(tokens[0].kind) == "TokenKind.identifier" and str(tokens[1].kind) == "TokenKind.assignment":
                variabletokens = tokens[2:]
            else:
                print("ERROR: Invalid sequence of tokens")

        if ((tokennum or tokenstring) and tokenend) or (tokenlogical or tokenarithmetic):
            if tokennum and tokenstring:
                stringvalidity = False
                expressionvalidity = False
                inputvalidity = False
                print("ERROR: string value cannot be compared to a int")
            elif (tokenlogical or tokenarithmetic) and not (tokennum or tokenstring):
                if tokenlogical:
                    trueorfalse = False
                    for tk in tokens:
                        if str(tk.text) == "t" or str(tk.text) == "f":
                            trueorfalse = True
                    if trueorfalse:
                        stringvalidity = False
                        inputvalidity = False
                    else:
                        print("ERROR: No valid operands in the expression")
                        inputvalidity = False
                else:
                    inputvalidity = False
            elif (tokennum and tokenend) and (tokenlogical or tokenarithmetic):

                stringvalidity = False
                inputvalidity = False

            elif (tokennum and tokenend) and not (tokenlogical or tokenarithmetic):

                stringvalidity = False
                inputvalidity = False


            elif (tokenstring and tokenend) and (tokenlogical or tokenarithmetic):
                expressionvalidity = False
                inputvalidity = False
            elif (tokenstring and tokenend) and not (tokenlogical or tokenarithmetic):
                expressionvalidity = False
                inputvalidity = False
        elif tokenidentifier and tokenassignment and not tokennum and not tokenstring and not tokenarithmetic and not tokenlogical:
            if str(tokens[0].kind) == "TokenKind.identifier" and str(tokens[1].kind) == "TokenKind.assignment" and str(tokens[2].kind) == "TokenKind.identifier":
                if str(tokens[2].text) in Global:
                    try:
                        transformint = float(Global[tokens[2].text])
                        inputvalidity = False
                        stringvalidity = False
                    except:
                        inputvalidity = False
                        expressionvalidity = False
        else:
            print("ERROR: not a valid sequence of characters")
            expressionvalidity = False
            stringvalidity = False
            inputvalidity = False


    output = [expressionvalidity, stringvalidity, variabletokens, inputvalidity]
    return output
