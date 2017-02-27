package main

import "fmt"

type Node struct {
    data int
    next * Node
}
func insert(h *Node, d *Node, p int) bool{  
    if h.next == nil {
        h.next = d
        return true
    }
    i := 0
    n := h
    for n.next != nil {
        i++
        if i == p {
            if n.next.next == nil {
                n.next = d
                return true
            } else {
                d.next = n.next
                n.next = d.next
                return true
            }
        }
        n = n.next
        if n.next == nil {
            n.next = d
            return true
        }
    }
    return false 
}  
func (h *Node) add(d *Node){
    n := h
    if n.next == nil {
        n.next = d
        return
    }
    for n.next != nil {
        n = n.next
        if n.next == nil {
            n.next = d
            return
        }
    }
    return

}
func (h *Node) revlinkedlist() (nh *Node){
    n := h 
    fmt.Println(h,nh) 
    nh.data = n.data
    nh.next = nil
    
    for n.next != nil {
        print(n.next.data,nh.next,nh)
        nh.data = n.next.data
        nh.next = nh
        n = n.next

    }
    
    return nh
}
func main(){
    var node Node
    for i := 1; i <= 10; i++ {
        var d Node
        d.data = i
        // insert(&node, &d, i)
        node.add(&d)
    }
    fmt.Println(node)
    // n := node
    // for n.next != nil {
    //     fmt.Println(*n.next)
    //     n = *n.next
    // }
    // revnode := node.revlinkedlist()
    // fmt.Println(revnode)
    // for revnode.next != nil {
    //     fmt.Println(*revnode.next)
    //     revnode = revnode.next
    // }
    fmt.Println("1"+string(2))
}
