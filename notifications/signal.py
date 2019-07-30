@receiver(post_save, sender=InAppMessage)
#will be called whenever an InAppMessage object is saved
def send_new_message_notification(sender, **kwargs):
    # the instance that is being saved is retrieved to have the ids of the users on both ends of the message
    message = kwargs['instance']
    send_new_message_push_notification(sender_id=message.sender.id,
                                       recipient_id=message.recipient.id,
                                       content=message.content)