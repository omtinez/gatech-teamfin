% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<p>This is TeamFin.</p>

<form action="/about" method="post" class="form-horizontal" role="form">
  <div class="form-group">
    <input value="Sync" type="submit" class="btn btn-primary active" style = #ff0080/>
  </div>
</form>
