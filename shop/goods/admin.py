from django.contrib import admin
from .models import Product, ProductProp, ProductPropsValue, Goods


class ProductPropsValueInline(admin.TabularInline):
    model = ProductPropsValue
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPropsValueInline]


@admin.register(ProductProp)
class ProductPropAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductPropsValue)
class ProductPropsValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    # fields = ["name", "description"]
    pass


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# @admin.register(Choice)
# class ChoiceAdmin(admin.ModelAdmin):
#     list_display = ('question', 'choice_text', 'votes',)
#     list_filter = ['question']
#
#
# # admin.site.register(Choice, ChoiceAdmin)
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     # fields = ['pub_date', 'question_text']
#     list_display = ('question_text', 'pub_date', 'was_published_recently')
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     inlines = [ChoiceInline]
#
#     list_filter = ['pub_date']
#     search_fields = ['question_text']
# # admin.site.register(Question, QuestionAdmin)
