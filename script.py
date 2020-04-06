def main():
    title = "father"
    name = "dvir"
    context = 'Tree T ("%s0"); \n' %(name)
    context += 'string father= ""; \n'


    for i in range(1, 35):
        context += 'father = "%s%s"; \n ' % (name,str(i))
        context += 'T.addFather("%s%s",father); \n' % (name,str(i - 1))
        out = title
        if i == 2:
            out = "grand" + out
        elif i > 2:
            out = "grand" + out
            for j in range(2, i):
                out = "great-" + out

        out = '"%s"' % out

        context += 'CHECK(T.relation(father) == string(%s)); \n\n' % (out)

    with open('Output2.txt', 'w') as f1:
        f1.write(context)

    title = "mother"
    context = 'Tree T ("%s0"); \n' % (name)
    context += 'string mother=""; \n'

    for i in range(1, 35):
        context += 'mother = "%s%s"; \n ' % (name,str(i))
        context += 'T.addMother("%s%s",mother); \n' % (name,str(i - 1))
        out = title
        if i == 2:
            out = "grand" + out
        elif i > 2:
            out = "grand" + out
            for j in range(2, i):
                out = "great-" + out

        out = '"%s"' % out

        context += 'CHECK(T.relation(mother) == string(%s)); \n\n' % (out)

    with open('Output3.txt', 'w') as f1:
        f1.write(context)

    context = 'Tree T ("%s0"); \n' % (name)

    title = "father"
    context += 'string father=""; \n'
    for i in range(1, 30):
        context += 'father = "%s%s"; \n ' % (name,str(i))
        context += 'T.addFather("%s%s",father); \n' % (name,str(i - 1))
        out = title
        if i == 2:
            out = "grand" + out
        elif i > 2:
            out = "grand" + out
            for j in range(2, i):
                out = "great-" + out

        out = '"%s"' % out

        context += 'CHECK(T.find(%s) == string("dvir%s")); \n\n' % (out, str(i))

    with open('Output4.txt', 'w') as f1:
        f1.write(context)


if __name__ == '__main__':
    main()