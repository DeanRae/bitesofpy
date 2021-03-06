## [Bite 29. Martin's IQ test](https://codechalleng.es/bites/29/)

<p>Martin is preparing to pass an IQ test.</p><p>The most frequent task in this test is to find out which one of the given characters differs from the others. He observed that one char usually differs from the others in being <i>alphanumeric</i> or not.</p><p>Please help Martin! To check his answers, he needs a program to find the <i>different</i> one (the alphanumeric among non-alphanumerics or vice versa) among the given characters.</p><p>Complete <code>get_index_different_char</code> to meet this goal. It receives a <code>chars list</code> and returns an <code>int index</code> (zero-based).<p>Just to be clear, alphanumeric == <code>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789</code></p><p>Examples:</p><pre>['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)
</pre><p>See the <i>TESTS</i> tab for more details</p>

Check out our full catalogue of Bites of Py [here](https://codechalleng.es/bites/catalogue).
