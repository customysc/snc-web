import http from "@/utils/axios";

export interface XWOrderItem {
  id?: number;
  name?: string;
  student_no?: string;
  department?: string;
  phone?: string;
  computer?: string;
  issue?: string;
  images?: string;
  appointment_time?: string;
  customer_notes?: string;
  attend_time?: string;
  start_time?: string;
  end_time?: string;
  status?: string;
  result?: string;
  resolution_method?: string;
  resolution_process?: string;
  resolution_images?: string;
  customer_feedback?: string;
}

export function getOrderPage(current_page = 1, page_size = 50) {
  return http.get("/xware/order/page", {
    params: { current_page, page_size },
  });
}

export function getOrderById(id: number) {
  return http.get(`/xware/order/${id}`);
}

export function addOrder(data: XWOrderItem) {
  return http.post("/xware/order/add", data);
}

export function updateOrder(data: XWOrderItem) {
  return http.post("/xware/order/update", data);
}

export function deleteOrder(id: number) {
  return http.post("/xware/order/delete", null, { params: { id } });
}

export function getSuggestions(field: string) {
  return http.get("/xware/order/suggestions", { params: { field } });
}
