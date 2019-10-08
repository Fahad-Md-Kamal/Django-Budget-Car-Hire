# import io
# from django.http import FileResponse
# from django.shortcuts import get_object_or_404

# from reportlab.pdfgen import canvas
# # from reportlab.lib.pagesizes import letter, landscape

# from datetime import datetime, date
# from .models import Fleet, Transaction


# def pdf_gen(request, pk):
#     fleet           = get_object_or_404(Fleet, pk= pk)
#     paid_fleet      = get_object_or_404(Transaction, fleet=fleet)
#     vehicles        = fleet.vehicles.all()

#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#     # p = canvas.Canvas(f'{fleet.fleet_ref}-invoice.pdf', pagesize=letter)
#     p.setLineWidth(.3)
#     p.setFont('Helvetica', 12)

#     # Center Text
#     p.setFont('Helvetica', 18, leading=None )
#     p.drawString(240, 790, 'Budget Car Hire' )
#     p.drawString(240, 540, 'Vehicle(s) Detail' )
#     p.setFont('Helvetica', 12, leading=None )
#     p.drawString(250, 765, 'Fleet Detail Report' )
#     # Left Side Information
#     p.drawString(30, 730, f'Customer Name : {fleet.user.user.username}' )
#     p.drawString(30, 710, f'Booked On : {fleet.booked_date.date()}' )
#     p.drawString(30, 690, f'Paid On : {paid_fleet.timestamp.date()}')
#     p.drawString(30, 670, f'Total Rent : {fleet.get_total()}/-')
#     # Right Side Information
#     p.drawRightString(550, 730,  f'{fleet.fleet_ref} : Reference ID' )
#     p.drawRightString(550, 710,  f'{fleet.approved_on.date()} : Start Date' )
#     p.drawRightString(550, 690,  f'{fleet.expiration_date().date()} : Expires On' )
#     p.drawRightString(550, 670,  f'{paid_fleet.token} : Token' )
#     for i in range(10,580):
#         p.drawString(i, 755, '. .')
#     for i in range(10,580):
#         p.drawString(i, 650, '. .')
#     # Vehicle Details
#     p.drawString(30, 500, 'Model')
#     p.drawString(150, 500, 'Reg. No.')
#     p.drawString(250, 500, 'Capacity')
#     p.drawString(350, 500, 'Rent/ Month')
#     p.drawString(490, 500, 'Vehicle Type')
#     for i in range(10,580):
#         p.drawString(i, 485, '. .')
#     y = 460
#     for car in vehicles:
#         p.drawString(30, y, car.get_model_name_display())
#         p.drawString(150, y, car.reg_no)
#         p.drawString(270, y, str(car.capacity))
#         p.drawString(360, y, str(car.rent))
#         p.drawString(500, y, car.get_vehicle_type_display())
#         y -= 20
#     for i in range(330,540):
#         p.drawString(i, 70, '. .')
#     # Bottom Right Corner
#     p.drawString(400, 120, 'Authorized by:')
#     p.drawString(400, 50, 'Budget Car Hire')
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename=f'{fleet.fleet_ref}-invoice.pdf')


