#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to base_interfaces_demo__srv__Addlnts_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Addlnts_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub num1: i32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub num2: i32,

}



impl Default for Addlnts_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Addlnts_Request::default())
  }
}

impl rosidl_runtime_rs::Message for Addlnts_Request {
  type RmwMsg = super::srv::rmw::Addlnts_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        num1: msg.num1,
        num2: msg.num2,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      num1: msg.num1,
      num2: msg.num2,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      num1: msg.num1,
      num2: msg.num2,
    }
  }
}


// Corresponds to base_interfaces_demo__srv__Addlnts_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Addlnts_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub sum: i32,

}



impl Default for Addlnts_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::Addlnts_Response::default())
  }
}

impl rosidl_runtime_rs::Message for Addlnts_Response {
  type RmwMsg = super::srv::rmw::Addlnts_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        sum: msg.sum,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      sum: msg.sum,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      sum: msg.sum,
    }
  }
}






#[link(name = "base_interfaces_demo__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__base_interfaces_demo__srv__Addlnts() -> *const std::ffi::c_void;
}

// Corresponds to base_interfaces_demo__srv__Addlnts
#[allow(missing_docs, non_camel_case_types)]
pub struct Addlnts;

impl rosidl_runtime_rs::Service for Addlnts {
    type Request = Addlnts_Request;
    type Response = Addlnts_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__base_interfaces_demo__srv__Addlnts() }
    }
}


