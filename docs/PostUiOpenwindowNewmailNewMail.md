# PostUiOpenwindowNewmailNewMail

new_mail object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | body string | 
**recipients** | **List[int]** | recipients array | 
**subject** | **str** | subject string | 
**to_corp_or_alliance_id** | **int** | to_corp_or_alliance_id integer | [optional] 
**to_mailing_list_id** | **int** | Corporations, alliances and mailing lists are all types of mailing groups. You may only send to one mailing group, at a time, so you may fill out either this field or the to_corp_or_alliance_ids field | [optional] 

## Example

```python
from esi_client.models.post_ui_openwindow_newmail_new_mail import PostUiOpenwindowNewmailNewMail

# TODO update the JSON string below
json = "{}"
# create an instance of PostUiOpenwindowNewmailNewMail from a JSON string
post_ui_openwindow_newmail_new_mail_instance = PostUiOpenwindowNewmailNewMail.from_json(json)
# print the JSON string representation of the object
print PostUiOpenwindowNewmailNewMail.to_json()

# convert the object into a dict
post_ui_openwindow_newmail_new_mail_dict = post_ui_openwindow_newmail_new_mail_instance.to_dict()
# create an instance of PostUiOpenwindowNewmailNewMail from a dict
post_ui_openwindow_newmail_new_mail_form_dict = post_ui_openwindow_newmail_new_mail.from_dict(post_ui_openwindow_newmail_new_mail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


