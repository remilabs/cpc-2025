for path in ./*; do
  [ ! -d path ] && continue
  verifyproblem "$path"
done
