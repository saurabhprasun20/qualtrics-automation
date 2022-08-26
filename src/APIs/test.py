from DeleteBlock import delete_block

def handle_delete(survey_id,default_block_id):
    respo = delete_block(str(survey_id), str(default_block_id)).json()
    return respo
