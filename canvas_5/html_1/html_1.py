@fused.udf
def udf(name: str = "$name"):
    from string import Template

    template = Template("""<h1> hello $name</h1>""")
    return """<script>
(function () {
  if (window.fusedCanvas) return;

  function send(type, parameter, values) {
    if (typeof parameter !== "string" || parameter.length === 0) {
      throw new Error("Canvas parameter name must be a non-empty string");
    }

    const message = { type: type, parameter: parameter, values: values };
    window.parent && window.parent.postMessage(message, "*");
  }

  window.fusedCanvas = {
    setParam: function (parameter, value) {
      send("param", parameter, value);
    },
    setParams: function (valuesByParameter) {
      if (!valuesByParameter || typeof valuesByParameter !== "object") {
        throw new Error("Canvas parameters must be an object");
      }

      Object.keys(valuesByParameter).forEach(function (parameter) {
        send("param", parameter, valuesByParameter[parameter]);
      });
    },
    clearParam: function (parameter) {
      send("clear", parameter, null);
    },
    clearAllParams: function () {
      send("clear", "_all", null);
    },
  };
})();
</script>
""" + template.safe_substitute(name=name)
