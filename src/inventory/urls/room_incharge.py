from django.urls import path
from inventory.views import room_incharge

app_name = 'room_incharge'

urlpatterns = [
    path('rooms/<slug:room_slug>/categories/', room_incharge.CategoryListView.as_view(), name='category_list'),
    path('rooms/<slug:room_slug>/categories/<slug:category_slug>/update/', room_incharge.CategoryUpdateView.as_view(), name='category_update'),
    path('rooms/<slug:room_slug>/categories/<slug:category_slug>/delete/', room_incharge.CategoryDeleteView.as_view(), name='category_delete'),
    path('rooms/<slug:room_slug>/categories/create/', room_incharge.CategoryCreateView.as_view(), name='category_create'),
    path('rooms/<slug:room_slug>/brands/', room_incharge.BrandListView.as_view(), name='brand_list'),
    path('rooms/<slug:room_slug>/brands/create/', room_incharge.BrandCreateView.as_view(), name='brand_create'),
    path('rooms/<slug:room_slug>/brands/<slug:brand_slug>/update/', room_incharge.BrandUpdateView.as_view(), name='brand_update'),
    path('rooms/<slug:room_slug>/brands/<slug:brand_slug>/delete/', room_incharge.BrandDeleteView.as_view(), name='brand_delete'),
    path('rooms/<slug:room_slug>/items/', room_incharge.ItemListView.as_view(), name='item_list'),
    path('rooms/<slug:room_slug>/items/create/', room_incharge.ItemCreateView.as_view(), name='item_create'),
    path('rooms/<slug:room_slug>/items/<slug:item_slug>/update/', room_incharge.ItemUpdateView.as_view(), name='item_update'),
    path('rooms/<slug:room_slug>/items/<slug:item_slug>/delete/', room_incharge.ItemDeleteView.as_view(), name='item_delete'),
    path('rooms/<slug:room_slug>/items/<slug:item_slug>/archive/', room_incharge.ItemArchiveView.as_view(), name='item_archive'),
    path('rooms/<slug:room_slug>/item-groups/', room_incharge.ItemGroupListView.as_view(), name='item_group_list'),
    path('rooms/<slug:room_slug>/item-groups/create/', room_incharge.ItemGroupCreateView.as_view(), name='item_group_create'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/update/', room_incharge.ItemGroupUpdateView.as_view(), name='item_group_update'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/delete/', room_incharge.ItemGroupDeleteView.as_view(), name='item_group_delete'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/items/create/', room_incharge.ItemGroupItemCreateView.as_view(), name='item_group_item_create'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/items/', room_incharge.ItemGroupItemListView.as_view(), name='item_group_item_list'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/items/<slug:item_group_item_slug>/update/', room_incharge.ItemGroupItemUpdateView.as_view(), name='item_group_item_update'),
    path('rooms/<slug:room_slug>/item-groups/<slug:item_group_slug>/items/<slug:item_group_item_slug>/delete/', room_incharge.ItemGroupItemDeleteView.as_view(), name='item_group_item_delete'),
    path('rooms/<slug:room_slug>/systems/', room_incharge.SystemListView.as_view(), name='system_list'),
    path('rooms/<slug:room_slug>/systems/create/', room_incharge.SystemCreateView.as_view(), name='system_create'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/update/', room_incharge.SystemUpdateView.as_view(), name='system_update'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/delete/', room_incharge.SystemDeleteView.as_view(), name='system_delete'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/components/', room_incharge.SystemComponentListView.as_view(), name='system_component_list'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/components/create/', room_incharge.SystemComponentCreateView.as_view(), name='system_component_create'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/components/<slug:component_slug>/update/', room_incharge.SystemComponentUpdateView.as_view(), name='system_component_update'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/components/<slug:component_slug>/delete/', room_incharge.SystemComponentDeleteView.as_view(), name='system_component_delete'),
    path('rooms/<slug:room_slug>/systems/<slug:system_slug>/components/<slug:component_slug>/archive/', room_incharge.SystemComponentArchiveView.as_view(), name='system_component_archive'),
    path('rooms/<slug:room_slug>/purchases/', room_incharge.PurchaseListView.as_view(), name='purchase_list'),
    path('rooms/<slug:room_slug>/purchases/create/', room_incharge.PurchaseCreateView.as_view(), name='purchase_create'),
    path('rooms/<slug:room_slug>/purchases/<slug:purchase_slug>/update/', room_incharge.PurchaseUpdateView.as_view(), name='purchase_update'),
    path('rooms/<slug:room_slug>/purchases/<slug:purchase_slug>/delete/', room_incharge.PurchaseDeleteView.as_view(), name='purchase_delete'),
    path('rooms/<slug:room_slug>/purchases/<slug:purchase_slug>/complete/', room_incharge.PurchaseCompleteView.as_view(), name='purchase_complete'),
    path('rooms/<slug:room_slug>/purchases/<slug:purchase_slug>/add_to_stock/', room_incharge.PurchaseAddToStockView.as_view(), name='purchase_add_to_stock'),
    path('rooms/<slug:room_slug>/purchases/new_item/create/', room_incharge.PurchaseNewItemCreateView.as_view(), name='purchase_new_item_create'),
    path('rooms/<slug:room_slug>/archives/', room_incharge.ArchiveListView.as_view(), name='archive_list'),
    path('rooms/<slug:room_slug>/dashboard/', room_incharge.RoomDashboardView.as_view(), name='room_dashboard'),
    path('rooms/<slug:room_slug>/update/', room_incharge.RoomUpdateView.as_view(), name='room_update'),
    path('rooms/<slug:room_slug>/issues/', room_incharge.IssueListView.as_view(), name='issue_list'),
    path('rooms/<slug:room_slug>/settings/', room_incharge.RoomSettingsView.as_view(), name='room_settings'),
    path('rooms/<slug:room_slug>/report/', room_incharge.RoomReportView.as_view(), name='room_report'),
]