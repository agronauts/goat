from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from lists.models import Item, List

User = get_user_model()


class ItemAndListModelTest(TestCase):
    def test_default_item_text(self):
        first_item = Item()
        self.assertEqual(first_item.text, '')

    def test_list_item_relationship(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_invalid_list_items_arent_saved(self):
        self.client.post('/lists/new', data={'text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

class ListModelTest(TestCase):

    def test_save_returns_new_list_object(self):
        returned = List.create_new(first_item_text='new item text')
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)

    def test_list_can_have_owner(self):
        List(owner=User()) # Should not raise

    def test_list_owner_is_optional(self):
        List().full_clean() # Should not raise

    def test_cannot_save_empty_list(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()
    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id,))

    def test_create_new_list_and_first_item(self):
        List.create_new(first_item_text='Spiritualism without religion')
        item = Item.objects.first()
        self.assertEqual(item.text, 'Spiritualism without religion')
        list_ = List.objects.first()
        self.assertEqual(item.list, list_)

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()
        List.create_new(first_item_text='Bruce Brueno', owner=user)
        list_ = List.objects.first()
        self.assertEqual(list_.owner, user)

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()

    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        first_item = Item.objects.create(text='EC', list=list_)
        second_item = Item.objects.create(text='SD', list=list_)
        self.assertEqual(list_.name, first_item.text)

    def test_CAN_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean()  # should not raise

    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )

    def test_string_representation(self):
        item = Item(text='Joe Abercrombie')
        self.assertEqual(str(item), 'Joe Abercrombie')

    def test_lists_can_have_owners(self):
        user = User.objects.create(email='andrew.bisharat@evenningsends.com')
        list_ = List.objects.create(owner=user)
        self.assertIn(list_, user.list_set.all())

    def test_list_owner_is_optional(self):
        List.objects.create()  # should not raise

    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='first item')
        Item.objects.create(list=list_, text='second item')
        self.assertEqual(list_.name, 'first item')
