from django.urls import path
from inventory.views import central_admin

app_name = 'central_admin'

urlpatterns = [
    path('', central_admin.DashboardView.as_view(), name='dashboard'),
    path('people/', central_admin.PeopleListView.as_view(), name='people_list'),
    path('people/create/', central_admin.PeopleCreateView.as_view(), name='people_create'),
    path('people/<slug:people_slug>/delete/', central_admin.PeopleDeleteView.as_view(), name='people_delete'),
    path('rooms/', central_admin.RoomListView.as_view(), name='room_list'),
    path('rooms/create/', central_admin.RoomCreateView.as_view(), name='room_create'),
    path('rooms/<slug:room_slug>/delete/', central_admin.RoomDeleteView.as_view(), name='room_delete'),
    path('rooms/<slug:room_slug>/update/', central_admin.RoomUpdateView.as_view(), name='room_update'),
    path('vendors/', central_admin.VendorListView.as_view(), name='vendor_list'),
    path('purchases/', central_admin.PurchaseListView.as_view(), name='purchase_list'),
    path('issues/', central_admin.IssueListView.as_view(), name='issue_list'),
    path('departments/', central_admin.DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', central_admin.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<slug:department_slug>/delete/', central_admin.DepartmentDeleteView.as_view(), name='department_delete'),
]
