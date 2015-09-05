
def results_to_array(result_set):
        contact_list = []
        for c in result_set:
            c_dict = c.__dict__
            if c_dict.has_key("_sa_instance_state"):
                del c_dict["_sa_instance_state"]
            contact_list.append(c_dict)

        return contact_list
