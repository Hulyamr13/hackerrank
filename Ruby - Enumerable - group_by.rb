def group_by_marks(marks, n)
      marks.group_by { |_, mark| mark >= n ? 'Passed' : 'Failed' }
end