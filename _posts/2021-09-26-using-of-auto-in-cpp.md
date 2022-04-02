---
layout: post
title:  "C++中auto的使用"
date: 2021-09-26 10:08:00 +0800
categories: dev
---
# C++中auto的使用

```cpp
// Basic 10-element integer array.
int x[10] = { 1, 2, 3, 4, 5, 6, 
              7, 8, 9, 10 };

// Range-based for loop to iterate 
// through the array.
// Access by value using a copy 
// declared as a specific type.
// Not preferred.
for( int y : x ) {         
    cout << y << " ";
}
cout << endl;

// The auto keyword causes type 
// inference to be used. 
// Preferred.

// Copy of 'x', almost always 
// undesirable
for( auto y : x ) { 
    cout << y << " ";
}
cout << endl;

// Type inference by reference.
// Observes and/or modifies in-place. 
// Preferred when modify is needed.
for( auto &y : x ) { 
    cout << y << " ";
}
cout << endl;
// Type inference by const reference.
// Observes in-place. 
// Preferred when no modify is needed.
for( const auto &y : x ) { 
    cout << y << " ";
}
```
