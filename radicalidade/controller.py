from datetime import date
from google.appengine._internal.django.utils.encoding import smart_str
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler, template
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Participante
import collections
import csv


class HomeHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/index.html', {}))

class RealizarPagamentoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/realizarPagamento.html', {}))

class InscricaoParticipanteHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoParticipante.html', {}))
    def post(self):
        
        try:
            participante = Participante()
            participante.nome = self.request.get('nome').strip().upper()
            participante.dataNascimento = self.request.get('dataNascimento')
            participante.sexo = self.request.get('sexo')
            participante.identidade = self.request.get('identidade')
            
            participante.logradouro = self.request.get('logradouro')
            participante.complemento = self.request.get('complemento')
            participante.cidade = self.request.get('cidade').strip().upper()
            participante.uf = self.request.get('uf')
            participante.bairro = self.request.get('bairro').strip().upper()
            
            participante.telCelular1 = self.request.get('telCelular1')
            participante.telCelular2 = self.request.get('telCelular2')
            participante.telResidencial = self.request.get('telResidencial')
            participante.email = self.request.get('email')
            
            participante.alergias = self.request.get('alergias')
            participante.medicamentos = self.request.get('medicamentos')
            
            participante.nomeContato = self.request.get('nomeContato')
            participante.telCelular1Contato = self.request.get('telCelular1Contato')
            participante.telCelular2Contato = self.request.get('telCelular2Contato')
            participante.telResidencialContato = self.request.get('telResidencialContato')
            participante.telComercialContato = self.request.get('telComercialContato')
            participante.ficouSabendo = self.request.get_all('ficouSabendo')

            participante.pagouInscricao = 'N'
            
            participanteJaExiste = Participante.all().filter('nome = ', participante.nome).count()
            if participanteJaExiste is None or participanteJaExiste == 0: 
                participante.put()
            
        except Exception, e:
            self.response.out.write(template.render('pages/errointerno.html', {}))
            return e
        
        return self.redirect('/realizarPagamento')

class LoginHandler(RequestHandler):
    def get(self):
        
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.out.write(template.render('pages/admin.html', {'usuarioLogado':user.nickname()}))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class LogoutHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            return self.redirect(users.create_logout_url('/'))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoParticipantesInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            results = Participante.all().order('nome')
            
            self.response.out.write(template.render('pages/reports/relacaoParticipantesInscritos.html',
                                                    {'listaItens':results, 'total':results.count()}))
         
class RelacaoEstatisticaParticipantesInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            
            totalParticipantes = Participante.all().count()
            totalFeminino = Participante.all().filter('sexo = ', 'F').count()
            totalMasculino = totalParticipantes - totalFeminino
            
            totalPaticipantesPagouInscricao = Participante.all().filter('pagouInscricao = ', 'S').count()
            totalPaticipantesNaoPagouInscricao = totalParticipantes - totalPaticipantesPagouInscricao
            
            participantesPorBairro = dict()
            for participante in Participante.all().filter('cidade = ', 'RIO DE JANEIRO').order('bairro'):
                qtde = participantesPorBairro.get(participante.bairro)
                if qtde:
                    participantesPorBairro[participante.bairro] = qtde + 1
                else:
                    participantesPorBairro[participante.bairro] = 1
            participantesPorBairro = collections.OrderedDict(sorted(participantesPorBairro.items()))
            
            participantesPorOutrasCidades = dict()
            for participante in Participante.all().filter('cidade != ', 'RIO DE JANEIRO'):
                qtde = participantesPorOutrasCidades.get(participante.cidade + '/' + participante.bairro)
                if qtde:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = qtde + 1
                else:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = 1
            participantesPorOutrasCidades = collections.OrderedDict(sorted(participantesPorOutrasCidades.items()))
                    
            participantesPorIdade = dict()
            for participante in Participante.all():
                today = date.today()
                idade = today.year - int(participante.dataNascimento.split('/')[2])
                qtde = participantesPorIdade.get(idade)
                if qtde:
                    participantesPorIdade[idade] = qtde + 1
                else:
                    participantesPorIdade[idade] = 1
            participantesPorIdade = collections.OrderedDict(sorted(participantesPorIdade.items()))
            
            self.response.out.write(template.render('pages/reports/relacaoEstatisticaParticipantesInscritos.html',
                                                    {'totalParticipantes':totalParticipantes,
                                                     'totalFeminino':totalFeminino,
                                                     'totalMasculino':totalMasculino,
                                                     'participantesPorBairro':participantesPorBairro,
                                                     'participantesPorOutrasCidades':participantesPorOutrasCidades,
                                                     'participantesPorIdade':participantesPorIdade,
                                                     'totalPaticipantesPagouInscricao':totalPaticipantesPagouInscricao,
                                                     'totalPaticipantesNaoPagouInscricao':totalPaticipantesNaoPagouInscricao
                                                     }))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class ExportarParticipantesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=participantes.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Data de Nascimento", "Sexo", "Identidade",
                             "Logradouro", "Complemento", "Cidade", "UF", "Bairro",
                             "Tel Celular1", "Tel Celular2", "Tel Residencial", "Email",
                             "Alergias", "Medicamentos",
                             "Nome do Contato",
                             "Tel Celular1 Contato", "Tel Celular2 Contato", "Tel Residencial Contato", "Tel Comercial Contato",
                             "Pagou a Inscricao"])
            
            for participante in Participante.all().order('nome'):
                writer.writerow([smart_str(participante.nome, encoding='ISO-8859-1'),
                                 smart_str(participante.dataNascimento, encoding='ISO-8859-1'),
                                 smart_str(participante.sexo, encoding='ISO-8859-1'),
                                 smart_str(participante.identidade, encoding='ISO-8859-1'),
                                 smart_str(participante.logradouro, encoding='ISO-8859-1'),
                                 smart_str(participante.complemento, encoding='ISO-8859-1'),
                                 smart_str(participante.cidade, encoding='ISO-8859-1'),
                                 smart_str(participante.uf, encoding='ISO-8859-1'),
                                 smart_str(participante.bairro, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencial, encoding='ISO-8859-1'),
                                 smart_str(participante.email, encoding='ISO-8859-1'),
                                 smart_str(participante.alergias, encoding='ISO-8859-1'),
                                 smart_str(participante.medicamentos, encoding='ISO-8859-1'),
                                 smart_str(participante.nomeContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencialContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telComercialContato, encoding='ISO-8859-1'),
                                 smart_str(participante.pagouInscricao, encoding='ISO-8859-1')
                                 ])

application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/inscricaoParticipante', InscricaoParticipanteHandler),
                                      ('/login', LoginHandler),
                                      ('/logout', LogoutHandler),
                                      ('/exportarParticipante', ExportarParticipantesHandler),
                                      ('/realizarPagamento', RealizarPagamentoHandler),
                                      ('/relacaoParticipantesInscritos', RelacaoParticipantesInscritosHandler),
                                      ('/relacaoEstatisticaParticipantesInscritos', RelacaoEstatisticaParticipantesInscritosHandler)
                                     ])
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
