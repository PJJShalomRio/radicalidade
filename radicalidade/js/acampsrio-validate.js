$(document).ready(function() {

	$('#dataNascimento').mask('00/00/0000');
	$('#telCelular1').mask('(00) 00000-0000');
	$('#telCelular2').mask('(00) 00000-0000');
	$('#telResidencial').mask('(00) 0000-0000');
	$('#telCelular1Contato').mask('(00) 00000-0000');
	$('#telCelular2Contato').mask('(00) 00000-0000');
	$('#telResidencialContato').mask('(00) 0000-0000');
	$('#telComercialContato').mask('(00) 0000-0000');

	$("#contatoForm").validate({
		rules : {
			nome : {
				required : true
			},
			telCelular1 : {
				required : true,
				minlength: 15
				
			},
			email : {
				required : true,
				email : true
			},
			comentario : {
				required : true
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório.",
				minlength: "Celular inválido."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			comentario : {
				required : "Campo obrigatório."
			}
		}
	});

	$("#inscricaoParticipanteForm").validate({
		rules : {
			nome : {
				required : true
			},
			dataNascimento : {
				required : true,
				dateBR : true
			},
			sexo : {
				required : true
			},
			identidade : {
				required : true
			},
			logradouro : {
				required : true
			},
			cidade : {
				required : true
			},
			bairro : {
				required : true
			},
			uf : {
				required : true
			},
			telCelular1 : {
				required : true,
				minlength: 15
			},
			telCelular2 : {
				minlength: 15
			},
			telResidencial : {
				minlength: 14
			},
			email : {
				required : true,
				email : true
			},
			nomeContato : {
				required : true
			},
			telCelular1Contato : {
				required : true,
				minlength: 15
			},
			telCelular2Contato : {
				minlength: 15
			},
			telResidencialContato : {
				minlength: 14
			},
			telComercialContato : {
				minlength: 14
			},
			termoCompromisso : {
				required : true
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			dataNascimento : {
				required : "Campo obrigatório.",
				dateBR : "Data de nascimento inválida."
			},
			sexo : {
				required : "Campo obrigatório."
			},
			identidade : {
				required : "Campo obrigatório."
			},
			logradouro : {
				required : "Campo obrigatório."
			},
			cidade : {
				required : "Campo obrigatório."
			},
			bairro : {
				required : "Campo obrigatório."
			},
			uf : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório.",
				minlength: "Celuar 1 inválido."
			},
			telCelular2 : {
				minlength: "Celular 2 inválido."
			},
			telResidencial : {
				minlength: "Telefone residencial inválido."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			nomeContato : {
				required : "Campo obrigatório."
			},
			telCelular1Contato : {
				required : "Campo obrigatório.",
				minlength: "Celular 1 inválido."
			},
			telCelular2Contato : {
				minlength: "Celular 2 inválido."
			},
			telResidencialContato : {
				minlength: "Telefone residencial inválido."
			},
			telComercialContato : {
				minlength: "Telefone comercial inválido."
			},
			termoCompromisso : {
				required : "A inscrição só será aceita se você concordar com todos os termos citados no contrato."
			}
		}
	});

	$("#inscricaoServicoForm").validate({
		rules : {
			nome : {
				required : true
			},
			dataNascimento : {
				required : true,
				dateBR : true
			},
			sexo : {
				required : true
			},
			logradouro : {
				required : true
			},
			cidade : {
				required : true
			},
			bairro : {
				required : true
			},
			uf : {
				required : true
			},
			telCelular1 : {
				required : true,
				minlength: 15
			},
			telCelular2 : {
				minlength: 15
			},
			telResidencial : {
				minlength: 14
			},
			email : {
				required : true,
				email : true
			},
			nomeContato : {
				required : true
			},
			telCelular1Contato : {
				required : true,
				minlength: 15
			},
			telCelular2Contato : {
				minlength: 15
			},
			telResidencialContato : {
				minlength: 14
			},
			telComercialContato : {
				minlength: 14
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			dataNascimento : {
				required : "Campo obrigatório.",
				dateBR : "Data de nascimento inválida."
			},
			sexo : {
				required : "Campo obrigatório."
			},
			logradouro : {
				required : "Campo obrigatório."
			},
			cidade : {
				required : "Campo obrigatório."
			},
			bairro : {
				required : "Campo obrigatório."
			},
			uf : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório.",
				minlength: "Celuar 1 inválido."
			},
			telCelular2 : {
				minlength: "Celular 2 inválido."
			},
			telResidencial : {
				minlength: "Telefone residencial inválido."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			nomeContato : {
				required : "Campo obrigatório."
			},
			telCelular1Contato : {
				required : "Campo obrigatório.",
				minlength: "Celular 1 inválido."
			},
			telCelular2Contato : {
				minlength: "Celular 2 inválido."
			},
			telResidencialContato : {
				minlength: "Telefone residencial inválido."
			},
			telComercialContato : {
				minlength: "Telefone comercial inválido."
			}
		}
	});
});