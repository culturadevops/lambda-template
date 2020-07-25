exports.handler = async event => {
    //esta variable se podra visualizar en el log del lambda
  console.log("log:" + process.env.primeravariable);

  const response = {
    statusCode: 200,
    //Esta variable sera enviada en la respuesta que retorna el lambda
    body: JSON.stringify(process.env.primeravariable)
  };
  return response;
};
