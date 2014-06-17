# This Python file uses the following encoding: utf-8
# ANOTAÇÃO PARA USAR CARACTERES ESPECIAIS AQUI. (MESMO PARA ANOTAÇÕES.)
""" 
@edsonlb
https://www.facebook.com/groups/pythonmania/
"""

from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q #Queries complexas
#from copa2014.models import Pessoa

def copaListar(request):
    jogo = Jogo.objects.all()[0:10]

    # TESTE LOCAL PARA VERIFICAR SE A TABELA ESTA LISTANDO
    #pessoas = []
    #pessoas.append(Pessoa(nome='NOME1', email='MAIL', telefone='TELEFONE'))
    #pessoas.append(Pessoa(nome='NOME2'))

    return render(request, 'copa2014/index.html', {'jogos': jogos})

def copaSalvar(request):
    if request.method == 'POST':

        try:
            jogo = Copa.objects.get(pk=codigo)
        except:
            jogo = Copa()

        jogo.gols1 = request.POST.get('gols1', '')
        jogo.gols2 = request.POST.get('gols2', '')
        jogo.gols3 = request.POST.get('gols3', '')
        jogo.gols4 = request.POST.get('gols4', '')
        jogo.gols5 = request.POST.get('gols5', '')
        jogo.gols6 = request.POST.get('gols6', '')

        jogo.save()
    return HttpResponseRedirect('/copa2014/')

def copaEditar(request, pk=0):
    try:
        jogo = Jogo.objects.get(pk=pk)
    except:
        return HttpResponseRedirect('/jogo/')

    return render(request, 'jogo/formPessoas.html', {'jogo': jogo})
