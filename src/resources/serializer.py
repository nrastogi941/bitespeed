from src.resources.model import Contact
from sqlalchemy import or_, false, case

def serialize_contact_data(parent_id):
    records = Contact.query.filter(
        or_(
            Contact.id == parent_id,
            Contact.linkedId == parent_id
        ),
        Contact.is_deleted == false()
    ).order_by(Contact.id).all()

    emails = []
    phone_number = []
    secondary_contact_ids = []
    for _record in records:
        if _record.email:
            emails.append(_record.email)
        if _record.phoneNumber:
            phone_number.append(_record.phoneNumber)
        if _record.linkPrecedence == "secondary":
            secondary_contact_ids.append(_record.id)

    return {
        "primaryContatctId": parent_id,
        "emails": emails,
        "phoneNumbers": phone_number,
        "secondaryContactIds": secondary_contact_ids
    }