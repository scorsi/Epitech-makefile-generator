#! /usr/bin/env python3

import sys
import os
import time


def usage():
    print("!WARNING!:\n")
    print("USAGE:")
    print("\t ./Make_generator\n")
    print("!WARNING END!")


def print_header(file, login, project):
    now = time.localtime(time.time())
    file.write("##\n")
    file.write("## Makefile for ")
    file.write(project)
    file.write(" in ")
    file.write(sys.path[0])
    file.write("\n")
    file.write("## \n")
    file.write("## Made by ")
    file.write(login)
    file.write("\n")
    file.write("## login   <")
    file.write(login)
    file.write("@epitech.net>\n")
    file.write("## \n")
    file.write("## Started on ")
    file.write(time.asctime(now))
    file.write(" ")
    file.write(login)
    file.write("\n")
    file.write("## Last update ")
    file.write(time.asctime(now))
    file.write(" ")
    file.write(login)
    file.write("\n")
    file.write("##\n\n")


def print_makefile(file, project):
    file.write("CC\t=\t")
    comp = input("quel compilateur voulez-vous ? (gcc clang...):")
    file.write(comp)
    file.write("\n\n")
    file.write("NAME\t=\t")
    file.write(project)
    file.write("\n\n")
    ask = input("utilisation de la lib lapin ? (y or n):")
    if ask == "y":
        lapin = ["-L/home/${USER}/.froot/include", "-llapin",
                 "-lsfml-audio", "-lsfml-graphics", "-lsfml_window", "-lsfml-system", "-lstdc++", "-ldl", "-lm"]
        file.write("LAPIN\t=\t-L/home/${USER}/.froot/lib\n")
        for car in lapin:
            file.write("LAPIN\t+=\t")
            file.write(car)
            file.write("\n")
        file.write("\n")
    file.write("CFLAGS\t=\t")
    flag = input("quels flags d'erreurs voulez-vous ? (-W -Wall...)\n")
    file.write(flag)
    while input("souhaitez-vous d'autres flags ? (y or n):") == "y":
        n_flag = input("entrez vos flags:\n")
        file.write("\n")
        file.write("CFLAGS +=\t")
        file.write(n_flag)
    file.write("\n\n")
    file.write("SRCS\t=\t\n\n")
    file.write("OBJS\t=\t$(SRCS:.c=.o)\n\n")
    file.write("RM\t=\trm -f\n\n")
    file.write("all: $(NAME)\n\n")
    file.write("$(NAME): $(OBJS)\n")
    file.write("\t$(CC) $(OBJS) -o $(NAME) $(CFLAGS)\n\n")
    file.write("clean:\n")
    file.write("\t$(RM) $(OBJS)\n\n")
    file.write("fclean: clean\n")
    file.write("\t$(RM) $(NAME)\n\n")
    file.write("re: fclean all\n\n")
    file.write(".phony: re fclean clean all")


if __name__ == "__main__":
    first = input("Est ce votre premier Makefile pour ce projet ? (y or n): ")
    if first == "y":
        login = input("quel est votre login: ")
        project = input("Quel est le nom du projet: ")
        try:
            os.remove("make.conf")
        except OSError:
            pass
        config = open("make.conf", "x")
        config.write(login)
        config.write("\n")
        config.write(project)
        config.write("\n")
        config.close()
    else:
        config = open("make.conf")
        login = config.readline()
        login = login.strip()
        project = config.readline()
        project = project.strip()
        config.close()
    header = input("Voulez vous un header ? (y or n): ")
    try:
        os.remove("Makefile")
    except OSError:
        pass
    file = open("Makefile", "x")
    if header == "y":
        print_header(file, login, project)
    print_makefile(file, project)
    file.close()
