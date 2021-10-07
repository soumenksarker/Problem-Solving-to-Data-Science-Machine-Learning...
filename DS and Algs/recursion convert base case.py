def to_string(n, base):
    convert_str = "0123456789ABCDEF"
            
    if n < base:
        return convert_str[n]
    
    else:
        n = n/base
        
        return convert_str[n]
