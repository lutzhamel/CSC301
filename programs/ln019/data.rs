struct Data<T> {
   value:T,   // T is a type variable
}

fn main() {
   // instantiating Data with i32 data
   let t:Data<i32> = Data{value:350};
   println!("value is :{} ",t.value);

   // instantiating Data with String data
   let t2:Data<String> = Data{value:"Tom".to_string()};
   println!("value is :{} ",t2.value);
}

