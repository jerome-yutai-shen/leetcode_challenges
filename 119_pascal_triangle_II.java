class Solution {
    public List<Integer> getRow(int rowIndex) {
            List<Integer> row =
        new ArrayList<>(rowIndex + 1) {
          {
            add(1);
          }
            };

        System.out.println("new row :" + row);


    for (int i = 0; i < rowIndex; i++) {
      for (int j = i; j > 0; j--) {
        row.set(j, row.get(j) + row.get(j - 1));
          System.out.println("row set:" + row);
      }
      row.add(1);
    }

    return row;
    }
}
