valid_languages = {'C', 'CPP', 'JAVA', 'PYTHON', 'PERL', 'PHP', 'RUBY', 'CSHARP', 'HASKELL', 'CLOJURE', 'BASH', 'SCALA',
                   'ERLANG', 'CLISP', 'LUA', 'BRAINFUCK', 'JAVASCRIPT', 'GO', 'D', 'OCAML', 'R', 'PASCAL', 'SBCL',
                   'DART', 'GROOVY', 'OBJECTIVEC'}

N = int(input())

for _ in range(N):
    api_id, language = input().split()
    if language in valid_languages:
        print("VALID")
    else:
        print("INVALID")
