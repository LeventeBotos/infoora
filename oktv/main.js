function eloallit(a, b, s) {
  let i = 1;
  let j = 1;
  let sa = new Array();
  let sb = new Array();
  //   console.log(a);
  //   console.log(b);
  //   console.log(s);
  //   console.log(s.length);
  let lenght = s.length;
  //   console.log(lenght);
  try {
    for (let k = 0; k < lenght; k++) {
      if (a >= s[k]) {
        sa[i] = s[k];
        i += 1;
        a = a - s[k];
      } else if (b >= s[k]) {
        sb[j] = s[k];
        j += 1;
        b = b - s[k];
      }
    }
  } catch (e) {
    console.error(e);
  }
  if (a > 0 || b > 0) {
    console.error("Hiba!");
    console.log(a);
    console.log(b);
  } else {
    console.log(sa);
    console.log(sb);
  }
}

// eloallit(14, 14, [7, 6, 5, 4, 3, 2, 1]);
eloallit(5, 11, [4, 5, 11, 2, 3, 1, 1, 1]);
// eloallit(14, 14, [7, 6, 5, 4, 3, 2, 1]);
