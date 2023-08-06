from django.shortcuts import render, redirect
from .models import ContractModel
from .forms import ContractForm
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q

def search_by(request):
    search = request.GET.get('search')
    if search:    
        contracts = ContractModel.objects.filter(
            Q(name__icontains=search) | 
            Q(rank__icontains=search) |
            Q(start_date__icontains=search) |
            Q(end_date__icontains=search) |
            Q(note__icontains=search) |
            Q(status__icontains=search) |
            Q(create_date__icontains=search)
        )
    else:      
        contracts = ContractModel.objects.all()
    return render(request, 'contract_list.html', {'all_contracts': contracts})

def order_by(request):
    order = request.GET.get('order')
    contracts = ContractModel.objects.all().order_by("-"+ order)
    if not order:
        order = 'default_field'
    order_selected = {str(order): 'btn-primary text-white'}
    # return render(request, 'contract_list.html', {'all_contracts': contracts, 'order_selected': order_selected})
    paginator = Paginator(contracts, 2) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contract_list.html', {'page_obj': page_obj, 'order_selected': order_selected})
  

@permission_required('hr_contracts.view_contractmodel', login_url='login')
def contract(request, contract_id):
	print('contract +++++++++++++++++++++++++++++++ ')
	if request.method == "GET":
		contract = ContractModel.objects.get(id=contract_id)
		return render(request,'contract_detail.html', {'contract': contract})

@login_required(login_url='login')
def all_contracts(request):
	print('all_contracts call +++++++++++++++++++++++++++ ')
	if request.method == "GET":
			print('all_contracts GET call')
			all_contracts = ContractModel.objects.all()
			all_contracts = ContractModel.objects.all()
			paginator = Paginator(all_contracts, 2) # ! Show 2 contacts per page.
			page_number = request.GET.get('page')
			page_obj = paginator.get_page(page_number)
			return render(request,'contract_list.html', {'page_obj': page_obj})
			# print('all_contracts ', all_contracts)
			# context = {'all_contracts': all_contracts}
			# return render(request,'contract_list.html', context)

@permission_required('hr_contracts.add_contractmodel', login_url='login') 
def add_contract(request):
		print('add_contract call +++++++++++++++++++++++++++++++++')
		if request.method == "GET":
				print('add_contract GET call')
				form = ContractForm()
				return render(request,'contract_create.html',{'form':form})
		if request.method == "POST" and request.FILES['attachment']:
				print('add_contract POST call++++++++++++++++++++++++++')
				print('++++++++++++++++++++++++++')
				form = ContractForm(request.POST, request.FILES)
				if form.is_valid():
					print('valid ++++++++++++++++++++++++++ ')
					name = form.cleaned_data.get('name')
					rank = form.cleaned_data.get('rank')
					start_date = form.cleaned_data.get('start_date')
					end_date = form.cleaned_data.get('end_date')
					note = form.cleaned_data.get('note')
					status = form.cleaned_data.get('status')
					is_active = form.cleaned_data.get('is_active')
					create_date = form.cleaned_data.get('create_date')
					attachment = form.cleaned_data.get('attachment')
					employee = form.cleaned_data.get('employee')
					tags = form.cleaned_data.get('tags')
					contract = ContractModel.objects.create(
						name=name,
						rank=rank,
						start_date=start_date,
						end_date=end_date,
						note=note,
						status=status,
						employee=employee,
						is_active=is_active,
						create_date=create_date,
						attachment=attachment
					)
					contract.tags.set(tags)
					contract.save()
					return redirect('/hr_contracts/show_contract/')

@permission_required('hr_contracts.change_contractmodel', login_url='login')  
def update_contract(request, contract_id):
		print('update_contract call')
		print('contract_id ', contract_id)
		print('contact update +++++++++++++++++++++++++++++++')
		contract = ContractModel.objects.get(id=contract_id)
		if request.method == "GET":
				print('update_contract GET call')
				values = {
					'name': contract.name,
					'rank': contract.rank,
					'start_date': contract.start_date,
					'end_date': contract.end_date,
					'note': contract.note,
					'status': contract.status,
					'is_active': contract.is_active,
					'create_date': contract.create_date,
					'attachment': contract.attachment,
					'employee': contract.employee,
            		'tags': contract.tags.all()
				}
				form = ContractForm(initial=values)
				context = {'form': form, 'uploaded_image': contract.attachment, 'contract': contract}
				return render(request, 'contract_update.html', context)
		elif request.method == "POST":
				print('update_contract POST call')
				print('data++++++++++++++++++')
				form = ContractForm(request.POST, request.FILES)
				if form.is_valid():
						print('form is_valid ++++++++++++++++++++++++++++++')
						contract.name = form.cleaned_data.get('name')
						contract.rank = form.cleaned_data.get('rank')
						contract.start_date = form.cleaned_data.get('start_date')
						contract.end_date = form.cleaned_data.get('end_date')
						contract.note = form.cleaned_data.get('note')
						contract.status = form.cleaned_data.get('status')
						contract.is_active = form.cleaned_data.get('is_active')
						contract.create_date = form.cleaned_data.get('create_date')
						if form.cleaned_data.get('attachment'):
							contract.attachment = form.cleaned_data.get('attachment')
						contract.employee = form.cleaned_data.get('employee')
						contract.tags.set(form.cleaned_data.get('tags'))
						contract.save()
						return redirect('/hr_contracts/detail/' + str(contract_id) + '/')

@permission_required('hr_contracts.delete_contractmodel', login_url='login')  
def delete_contract(request, contract_id):
		(print('delete_contract +++++++++++++++++++++++++++++++++ '))
		if request.method == "GET":
			contract = ContractModel.objects.get(id=contract_id)
		# 	return render(request, 'contract_delete.html', {'contract': contract})
		# if request.method == "POST":
		# contract = ContractModel.objects.filter(id=contract_id)
			contract.delete()
			return redirect('/hr_contracts/show_contract/')