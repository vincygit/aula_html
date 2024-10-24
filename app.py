from flask import (Flask, flash, redirect, render_template, request, url_for) # importa o flask

app = Flask(__name__) # cria uma instância
app.secret_key = 'segredo'  # Para utilizar flash messages

@app.route("/<string:nome>", methods=('GET' ,)) # Assina uma rota
def index(nome): # Função rsponsável pela página
    # HTML retornado
    return render_template('index.html', nome=nome)

@app.route("/galeria", methods=('GET' ,))
def galeria():
    return render_template('galeria.html')

@app.route("/contato", methods=('GET' ,))
def contato():
    return render_template('contato.html')

@app.route("/sobre", methods=('GET' ,))
def sobre():
    return render_template('sobre.html')

@app.route("/personagens", methods=('GET' ,))
def personagens():
    per1 = request.args.get('per1')
    per2 = request.args.get('per2')
    per3 = request.args.get('per3')
    return render_template('personagens.html', per1=per1, per2=per2, per3=per3)

@app.route("/area", methods=('GET' ,))
def area():
    altura = float(request.args.get('a'))
    largura = float(request.args.get('l'))
    area_calculada = largura * altura
    return render_template('area.html', altura=altura, largura=largura, area_calculada=area_calculada)
    
@app.route("/parouimpar/<string:n>", methods=('GET',))
def parouimpar(n):
    num = int(n)
    if num % 2 == 0:
        resultado = f"O número {n} é par!"
    else:
        resultado = f"O número {n} é ímpar!"
    return render_template('parouimpar.html', resultado=resultado)

@app.route("/nomecompleto/<string:nome>/<string:sobrenome>", methods=('GET',))
def nomecompleto(nome, sobrenome):
    return render_template('nomecompleto.html', nome=nome, sobrenome=sobrenome)

@app.route("/potencial/<string:n1>/<string:n2>", methods=('GET' ,))
def potencial(n1, n2):
    r = float(n1) ** float(n2)
    return render_template('potencial.html', n1=n1, n2=n2, resultado=r)


@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=("GET" , ))
def tabuada(numero = None): # Desobriga o valor

    if 'numero' in request.args: # se arguento existir
        numero = int(request.args.get('numero')) # atualiza numero

    return render_template('tabuada.html', numero=numero)  


@app.route('/calculojuros', methods=['GET', 'POST'])
def calculo_juros():
    if request.method == 'POST':
        try:
            investimento_inicial = float(request.form['investimento_inicial'])
            juros_ano = float(request.form['juros_ano'])
            tempo_meses = int(request.form['tempo_meses'])
            aporte_mensal = float(request.form['aporte_mensal'])

            # Cálculo de juros
            juros_mensal = juros_ano / 12 / 100
            total = investimento_inicial

            for _ in range(tempo_meses):
                total += aporte_mensal
                total *= (1 + juros_mensal)

            return render_template('calculo_juros.html', total=total)
        except ValueError:
            return render_template('calculo_juros.html', error="Por favor, insira valores válidos.")

    return render_template('calculo_juros.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        # Verificação de credenciais
        if email == 'aluno@senai.br' and senha == 'senai':
            flash('Usuário Logado com Sucesso!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Usuário ou senha incorretos, tente novamente.', 'error')

    return render_template('login.html')