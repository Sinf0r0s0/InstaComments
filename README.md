# InstaComments

This small API returns a list with (username / comment) of an Instagram post.

___

* Requeriments:

    **Requests**

* usage:

    By default, about 40 latest comments are loaded. (apparently the amount of comments is based on the size of the json) but you can select any maximum value:)

    **InstaComments(uri=uri, max_com=60, timeout=10 )**
    
    * **uri** = short code from instagram media
    * **max_com** = max comment loaded (optional)
    * **timeout** = requests connection timeout (optional)
    
    **InstaComments.get_query_hash()**
    * get query_hash, used on all requests
    
    **InstaComments.start(query_hash="f0986789a5c5d17c2400faebf16efd0d")**
    * **query_hash** = previously recovered (**optional**)
    * Returns the list of comments, eg:
      
         [{'glenn.liddel': 'Shocking'}, {'youngpablo522': 'nice job'}, ...}]
    
    
    
* Example:
    
    just this:

        post = 'B7XA4vblU4o'
        inst = InstaComments(post, 60)
        print(inst.start())

    or:

        post = 'B7XA4vblU4o'print()
        inst = InstaComments(post, 60)
        #  save the query_hash in some text file because it is permanent
        qh = inst.get_query_hash()
        print(inst.start(qh))

    or even (better):

        post = 'B7XA4vblU4o'
        inst = InstaComments(post, 60)
        print(inst.start("f0986789a5c5d17c2400faebf16efd0d"))
