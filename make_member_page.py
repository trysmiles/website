import os

with open("members/index.md", "w") as outf:
    outf.write('---\nlayout: default\n---\n')


    n = 0
    subtitle = ""
    peeps = []
    peepcodes = []
    for line in open("members.txt"):
        if line in [
            "PI\n",
            "postdoctoral researchers\n",
            "graduate researchers\n",
            "undergraduate researchers\n",
            "visitors\n",
            "alumni\n",
        ]:
            if n > 0:
                outf.write("# {}\n".format(subtitle.title()))
                outf.write("|      |      |      |\n")
                outf.write("|:----:|:----:|:----:|\n")
                for i in range(len(peeps))[::3]:
                    my_peeps = peeps[i: i + 3]
                    my_peepcodes = peepcodes[i: i + 3]
                    images = ""
                    names = ""
                    for j in range(3):
                        if j < len(my_peeps):
                            if not os.path.exists("assets/_member_imgs/{}.png".format(my_peepcodes[j])):
                                raise FileNotFoundError("File _member/imgs/{}.png does not exist.".format(my_peepcodes[j]))
                            if not os.path.exists("./members/{}.md".format(my_peepcodes[j])):
                                raise FileNotFoundError("./members/{}.md does not exist.".format(my_peepcodes[j]))
                            images += "|<a href='/website/members/{}'><img src='/website/assets/_member_imgs/{}.png' style='height:200px'></a>".format(my_peepcodes[j], my_peepcodes[j])
                            names += '|<a href="/website/members/{}">{}</a>'.format(
                                my_peepcodes[j], my_peeps[j]
                            )
                        else:
                            images += "| "
                            names += "| "
                    images += "|\n"
                    names += "|\n"
                    outf.write(images)
                    outf.write(names)
            n = 0
            subtitle = line
            peeps = []
            peepcodes = []
        elif line!='\n':
            line = line.strip("\n").strip(" - ")
            peeps.append(line)
            peepcodes.append(line.lower().replace(" ", "_"))
            n += 1
