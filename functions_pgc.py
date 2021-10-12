def sort_dict(d, **kwargs):
    by = 'value'
    reverse = True
    
    if 'by' in kwargs:
        by=kwargs['by']
    
    if 'reverse' in kwargs:
        reverse=kwargs['reverse']
    
    if by == 'value':
        return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
    if by == 'key':
        return dict(sorted(d.items(), key=lambda x: x[0], reverse=reverse)) 
